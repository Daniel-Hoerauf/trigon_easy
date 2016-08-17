# Trigon Engineering Society
#### The website for the Trigon Engineering Society at UVA

### Local Installation
The website is built using the python Flask framework. It's built using docker-compsoe for ease of portability and cross platform support, with grunt to compile the SASS files into CSS.

In order to get the website running locally, the first step is to compile the .scss files to .css files. To do this you must have [Ruby](https://www.ruby-lang.org/en/documentation/installation/) and [Nodejs](https://nodejs.org/en/download/package-manager/) install. Then, run the following commands
```bash
gem install                 # Might need to be run as root depending on your system
npm install -g grunt-cli
npm install                 # Run from project root
grunt sass
```
If you are making changes to the styling, rather than running `grunt sass` with every change you can simply run `grunt watch` to recompile the css files to every change in the static/scss/ directory

Once the scss files have been compiled, you must install [docker-compose](https://docs.docker.com/compose/install/) if it's not already present on your system.

Then, once docker-compose has been installed and the docker daemon is running, the site can be launched with the command
```bash
docker-compose up
```
If you've made any changes to the source code, the site image must be rebuilt on startup by running 
```bash
docker-compose up --build
```

Once the image is built and running the website can be seen at http://localhost:5000

###Consideration for Docker-machine
**Note:** if running on Windows or OSX and using docker-machine instead of Docker native, the IP address will not be `localhost`
You can find the IP by running
```
docker-machine ip <MACHINE_NAME>
```
Where `<MACHINE_NAME>` will be `default` unless you're running multiple docker-machines
