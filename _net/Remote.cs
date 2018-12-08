using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.Remoting.Channels.Tcp;

namespace RemotingSample
{
  public class RemoteXmas : MarshalByRefObject
  {
    public string Santa()    // add
    {
      Console.WriteLine("Santa called");
      return System.IO.File.ReadAllText(@"./success");
    }

  }
}
