# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
   config.vm.box = "bento/ubuntu-16.04"

   config.vm.provision :shell, path: "vagrant-setup/provision.sh", privileged: false

   config.ssh.forward_agent = true

   config.vm.synced_folder '.', '/vagrant'
end

