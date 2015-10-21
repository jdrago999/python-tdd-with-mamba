#!/usr/bin/env ruby
#^syntax detection

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # vagrant-berkshelf is incompatible with vagrant-librarian-chef
  if Vagrant.has_plugin?('vagrant-berkshelf')
    config.berkshelf.enabled = false
  end

  app_name = File.split(Dir.getwd)[-1]
  config.vm.synced_folder "./", "/var/www/#{app_name}"

  config.omnibus.chef_version = :latest
  config.librarian_chef.cheffile_dir = 'chef'
  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path = [ 'chef/cookbooks', 'chef/site-cookbooks' ]
    chef.run_list = ['foobar::default']
    chef.json = { }
  end

end
