BootStrap: docker
From: ubuntu # We are building an ubuntu-based image

%test
    echo "hello from test" "$@"

%environment
export LC_ALL=C # Specification of environment variables

%post
export DEBIAN_FRONTEND=noninteractive

# Some generic Ubuntu libraries
apt-get update
apt-get install -y libhdf5-dev locales python3-dev python3-pip curl
apt-get clean

# Python requirements
pip3 install pandas
pip3 install scikit-learn
