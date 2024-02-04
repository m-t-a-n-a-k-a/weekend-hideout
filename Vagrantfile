# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.provider "virtualbox" do |vb|
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end
  
  [
    {
      hostname: "extfw0101",
      memory: "512",
      segment_list: [
        { type: "global", addr: "192.168.201.11" },  
        { type: "dmz", addr: "192.168.202.11" },  
        { type: "internal", addr: "192.168.203.11" }
      ],
      gateway_list: [],
      site: "site01"
    },
    {
      hostname: "extfw0102",
      memory: "512",
      segment_list: [
        { type: "global", addr: "192.168.201.12" },  
        { type: "dmz", addr: "192.168.202.12" },  
        { type: "internal", addr: "192.168.203.12" }
      ],
      gateway_list: [],
      site: "site01"
    }
  ].each do |node|
    config.vm.define node[:hostname] do |i|
      i.vm.hostname = node[:hostname]
  
      i.vm.provider "virtualbox" do |vb|
        vb.memory = node[:memory]
      end

      node[:segment_list].each do |segment|
        i.vm.network "private_network", ip: segment[:addr], virtualbox__intnet: segment[:type]
      end

      node[:gateway_list].each do |gateway|
        i.vm.provision :shell, inline: "ip r add #{gateway[:destination]} via #{gateway[:gateway_addr]}"
      end

      i.vm.provision "ansible_local" do |ansible|
        ansible.install_mode = "pip"
        ansible.version = "8.5.0"
        ansible.playbook = "ansible/site.yml"
        ansible.inventory_path = "ansible/inventories/#{node[:site]}/hosts"
        ansible.galaxy_role_file = "ansible/requirements.yml"
        ansible.limit = node[:hostname]
      end 
    end
  end
end
