# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "docker"
  config.vbguest.auto_update = false

  config.vm.network "private_network", ip: "192.168.10.10"

  config.vm.provider "virtualbox" do |v|
    v.cpus = 1
    v.memory = 2048
  end

  if RUBY_PLATFORM.downcase =~ /mswin(?!ce)|mingw|cygwin|bccwin/
    # ignore executable bit for synced files
    config.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777","fmode=666"]
  end

 config.vm.provision 'shell', path: 'fig-setup.sh'

end
