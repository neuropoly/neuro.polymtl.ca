# Neuropoly Workstations

<!-- TODO: port from https://www.neuro.polymtl.ca/internal_resources/list_of_computers -->

## Connecting to Neuropoly Remotely

### VPN

First, you need to connect to [the VPN](http://www.polymtl.ca/si/reseaux/acces-securise-rvp-ou-vpn).

* Windows: ...
* Mac: ...
* Linux: `openconnect ...`

# ...

# ...

# SSH Shortcut

Add this to your `~/.ssh/config` file to allow you to just type `ssh joplin` or any other host and be connected to the right place with the right username:

```
Host joplin
HostName joplin.neuro.polymtl.ca

Host ferguson
HostName ferguson.neuro.polymtl.ca

Host abbey
HostName abbey.neuro.polymtl.ca

Host bireli
HostName bireli.neuro.polymtl.ca

Host rosenberg
HostName rosenberg.neuro.polymtl.ca

Host romane
HostName romane.neuro.polymtl.ca

Host tristano
HostName tristano.neuro.polymtl.ca

Host data
HostName data.neuro.polymtl.ca
User git

Match host *.neuro.polymtl.ca
User <POLYGRAMES_USERNAME>
```

Add this to your `~/.ssh/config` to make multiple ssh connections faster and without retyping your password:

```
Host *
ControlMaster auto
ControlPath ~/.ssh/%r@%h:%p
ControlPersist 3s
```

## Computing Stations

