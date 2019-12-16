# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.
Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "20190119.0.0"
  config.vm.network "private_network", ip: "10.10.0.5"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.hostname = "challenge"

  config.vm.provision "bootstrap", type: "shell", run: "once" do |s|
    s.inline = "apt update"
    s.inline = "apt install python python3 -y"
  end

  # Disable the new default behavior introduced in Vagrant 1.7, to
  # ensure that all Vagrant machines will use the same SSH key pair.
  # See https://github.com/mitchellh/vagrant/issues/5005
  config.ssh.insert_key = false

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "ansible/playbook.yml"
  end
end
