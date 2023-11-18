# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.ssh.forward_agent = true # So that boxes don't have to setup key-less ssh
  config.ssh.insert_key = false # To generate a new ssh key and don't use the default Vagrant one

  vars = { 
     "KAFKA_VERSION" => "2.8.0",
     "KAFKA_NAME" => "kafka_2.11-$KAFKA_VERSION",
     "KAFKA_TARGET" => "/vagrant/tars/",
     "KAFKA_HOME" => "$HOME/$KAFKA_NAME"
  }

  # escape environment variables to be loaded to /etc/profile.d/
  as_str = vars.map{|k,str| ["export #{k}=#{str.gsub '$', '\$'}"] }.join("\n")

  # common provisioning for all 
  config.vm.provision "shell", path: "scripts/hosts-file-setup.sh", env: vars
  config.vm.provision "shell", inline: "echo \"#{as_str}\" > /etc/profile.d/kafka_vagrant_env.sh", run: "always"
  config.vm.provision "shell", path: "scripts/init.sh", env: vars
 
  # configure zookeeper cluster
  (1..3).each do |i|
    config.vm.define "zookeeper#{i}" do |s|
      s.vm.hostname = "zookeeper#{i}"
      s.vm.network "private_network", ip: "192.168.56.#{i+1}"
      s.vm.provision "shell", run: "always", path: "scripts/zookeeper.sh", args:"#{i}", privileged: false, env: vars
      s.vm.provision "shell", run: "always", path: "scripts/broker.sh", args:"#{i}", privileged: false, env: vars
      
      s.trigger.after :up do |trigger|
        trigger.only_on = ["zookeeper3"] 
        trigger.run = {path: "scripts/zk.sh"}
      end
    end
  end



end
