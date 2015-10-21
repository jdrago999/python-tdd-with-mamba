
include_recipe 'apt'

package 'python'
package 'libpython-dev'
package 'python-pip'

%w(
  mamba
  expects
  doublex-expects
  doublex
).each do |pkg|
  bash "install #{pkg} python module" do
    code "pip install #{pkg}"
  end
end
