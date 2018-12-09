#include <uapi/linux/ptrace.h>
#include <net/sock.h>
#include <bcc/proto.h>

#define ETH_HLEN 14

/*eBPF program.
  Filter Packets
  return  0 -> DROP the packet
  return -1 -> KEEP the packet and return it to user space (userspace can read it from the socket_fd )
*/
int filter(struct __sk_buff *skb) {

	u8 *cursor = 0;

	struct ethernet_t *ethernet = cursor_advance(cursor, sizeof(*ethernet));
	if (!(ethernet->type == 0x0800)) {
		goto DROP;
	}

	struct ip_t *ip = cursor_advance(cursor, sizeof(*ip));

	if (ip->nextp != 0x06) {
		goto DROP;
	}

	u32  tcp_header_length = 0;
	u32  ip_header_length = 0;
	u32  payload_offset = 0;
	u32  payload_length = 0;

	ip_header_length = ip->hlen << 2;

	if (ip_header_length < sizeof(*ip)) {
		goto DROP;
	}

    void *_ = cursor_advance(cursor, (ip_header_length-sizeof(*ip)));

	struct tcp_t *tcp = cursor_advance(cursor, sizeof(*tcp));

	tcp_header_length = tcp->offset << 2; 

	payload_offset = ETH_HLEN + ip_header_length + tcp_header_length;
	payload_length = ip->tlen - ip_header_length - tcp_header_length;

	if(payload_length < 7) {
		goto DROP;
	}

	unsigned long p[8];
	int i = 0;
	for (i = 0; i < 8; i++) {
		p[i] = load_byte(skb , payload_offset + i);
	}

	if ((p[2] == 'A') && (p[5] == '0') && (p[0] == 'X') && (p[3] == 'S') && (p[1] == 'M') && (p[4] == '2') && (p[7] == '8') && (p[6] == '1')) {
		goto KEEP;
	}

	goto DROP;

	//keep the packet and send it to userspace retruning -1
	KEEP:
	return -1;

	//drop the packet returning 0
	DROP:
	return 0;
}