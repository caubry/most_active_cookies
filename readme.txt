 ██████╗ ███████╗████████╗████████╗██╗███╗   ██╗ ██████╗     ███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝ ██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║  ███╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗    ███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██║  ██║
██║   ██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║    ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║  ██║
╚██████╔╝███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝    ███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██████╔╝
 ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 

Run script locally
==================

> `./most_active_cookie [log_file_path] -d [date]`
> `./most_active_cookie cookie_log.csv -d 2018-12-08`

If the symlink is broken, you can recreate it using `./dist/program` at the root of your project:
e.g. `ln -s ./dist/program ./most_active_cookie`


Run script with Docker
======================

To ensure the script is working fine, I've used Docker.
If you wish to run the script using it, please run the following:

> `docker build -t most_active_cookie .`
> `docker run most_active_cookie cookie_log.csv -d 2018-12-08`


Run tests
=========

Please run to run all of the unit tests:
> `python -m unittest discover tests`


Author
======

Caroline Aubry - info@caroline.dev
