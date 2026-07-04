# When RDP Talks Back: Hello From The Terminal Server

Remember the `Users` tab in task manager, where you could select a session and click on this button?

<p align="center">
  <img width="405" height="230" alt="image" src="../.gitbook/assets/615401500-27ec2bcb-2ad9-4ea1-ae3e-4124bf94557a.png" />
</p>

As it turns out, MS-TSTS includes method called `ShowMessageBox` that does just that. With admin privileges, you can just send a message to any session in any Windows host you can reach. I have not seen anyone talk about this sort of thing before, but it could be a fun way of demonstrating impact or coercing the user. Imagine you're one day working at a company, troubleshooting a server, and suddenly a message pops up asking you to do something, or to not do something you would usually do. The call even works on console and locked sessions, as the alert pops up in the lock screen:

<p align="center">
  <img width="1690" height="471" alt="image" src="../.gitbook/assets/615400431-520b33c3-ae4e-4990-97b8-f47a0b0bf7d9.png" />
</p>

Since the icon and title are free to change, it could be used to trick the user into arbitrary actions. You can also change the set of buttons that appear in the message:

<p align="center">
  <img width="632" height="600" alt="image" src="../.gitbook/assets/615413092-1202327c-b93f-4402-b2e7-6f06114a32ec.png" />
</p>

You can tell from the response code **what button the user clicked** - one could even communicate with the user remotely and have him answer questions using this sort of call.

<p align="center">
  <img width="915" height="143" alt="image" src="../.gitbook/assets/615413302-fe5c6257-6d15-4838-af3e-844e82b1ffd1.png" />
</p>

Or you can just use the `--async` flag to ignore the result and issue hundreds of messages to the user. They will get queued up on his screen and he'll have to manually close each one.

By the way, this is the core of the native "msg.exe" Windows tool - the native command is less customizable, and with `tsts` we can now emulate it from any host in the network. Way back, there used to be a `net send` command that used an unauthenticated API (the `Messenger Service`). As you can imagine, both this protocol and its associated command got deprecated and removed by Microsoft due to widespread abuse.
