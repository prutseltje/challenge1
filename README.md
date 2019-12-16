# Running the test environment:
Clone this repo to your local system

## Installing requirements:

Ensure you have the following requirements installed on your test machine:
  - python(3)-pip   (via homebrew for osx or linux package manager)
  - vagrant         (https://www.vagrantup.com/downloads.html)
  - virtualbox 6.0  (https://www.virtualbox.org/wiki/Download_Old_Builds_6_0)

To install the requred pip packages run:
```bash
pip install -r requirements.txt
```

## Deploy:

From the folder containing the 'Vagrantfile':
```bash
vagrant up --provision
```

## To test the round-robin loadbalancer and webservers:

Start the python test script:
```bash
python check.py
```

### Note:
This config is tested on mac osx 10.15.1, vagrant 2.2.6 and virtualbox 6.0
