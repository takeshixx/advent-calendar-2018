using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Tcp;

namespace RemotingSample
{
  class Client
  {
    static void Main(string[] args)
    {
      // create and register the TCP channel
      // please note that I have set the security of the channel to false
      TcpChannel clientRemotingChannel = new TcpChannel();
      ChannelServices.RegisterChannel(clientRemotingChannel, false);

      // create an object of type RemothXmas
      // we have to do a cast because Activator.GetObject returns an object (doh)
      // type is RemoteXmas and server address is what we created in Server.cs (port:8888 and rXmas)

      // Server.cs code:
      // TcpChannel remotingChannel = new TcpChannel(8888);
      // ChannelServices.RegisterChannel(remotingChannel, false);
      // WellKnownServiceTypeEntry remoteObject = new WellKnownServiceTypeEntry(typeof(RemoteXmas), "rMxas", WellKnownObjectMode.SingleCall);

      RemoteXmas remoteXmasObject = (RemoteXmas)Activator.GetObject(typeof(RemoteXmas), "tcp://xmas.rip:10/rXmas");

      // now we can call Add and Sub functions
      Console.WriteLine("Calling Santa function \n{0}", remoteXmasObject.Santa());

      Console.WriteLine("Press any key to exit");
      Console.ReadLine();
    }
  }
}
