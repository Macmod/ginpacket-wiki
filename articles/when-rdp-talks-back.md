---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 🖥️ When RDP Talks Back: Hello From The Terminal Server

Remember the `Users` tab in Task Manager, where you could select a session and click on this button?

<figure><img src="../.gitbook/assets/615401500-27ec2bcb-2ad9-4ea1-ae3e-4124bf94557a.png" alt=""><figcaption></figcaption></figure>

As it turns out, [MS-TSTS](https://winprotocoldoc.z19.web.core.windows.net/MS-TSTS/[MS-TSTS].pdf) includes a method called `ShowMessageBox` that does just that - with admin privileges, you can just send a message to any session on any Windows host you can reach:

<figure><img src="../.gitbook/assets/615392593-031b92cc-ec3e-4c4b-8441-607c46b3748c.png" alt=""><figcaption></figcaption></figure>

I have not seen anyone talk about this sort of thing before, but it could be a fun way of demonstrating impact or coercing the user. Imagine you're one day working at a company, troubleshooting a server, and suddenly a message pops up asking you to do something, or to not do something you would usually do. The call even works on console and locked sessions, as the alert pops up on the lock screen:

<figure><img src="../.gitbook/assets/615400431-520b33c3-ae4e-4990-97b8-f47a0b0bf7d9.png" alt=""><figcaption></figcaption></figure>

Since the icon, title and buttons are also free to change (`szTitle`, `ulStyle`, controlled via `--buttons`/`-b` and `--icon`/`-i`), it could be used to trick the user into arbitrary actions. Some examples:

<figure><img src="../.gitbook/assets/615413092-1202327c-b93f-4402-b2e7-6f06114a32ec.png" alt=""><figcaption></figcaption></figure>

You can tell from the response code **what button the user clicked** - one could even communicate with the user remotely and have them answer questions using this sort of call.

<figure><img src="../.gitbook/assets/615413302-fe5c6257-6d15-4838-af3e-844e82b1ffd1.png" alt=""><figcaption></figcaption></figure>

Or you can just use the `--async` flag (which maps to `bDoNotWait`) to ignore the result and issue hundreds of messages to the user. They will get queued up on their screen and they'll have to manually close each one.

By the way, this is the core of the native "msg.exe" Windows tool - the native command is less customizable, and with `tsts` we can now emulate it from any host on the network. Way back, there used to be a `net send` command that used an unauthenticated API (the `Messenger Service`). As you can imagine, both this protocol and its associated command got deprecated and removed by Microsoft due to widespread abuse.
