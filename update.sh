# absolute path for this script
script_dir=$(cd $(dirname $0); pwd)

cd $script_dir
git pull origin master

cd ../agent
git pull origin master

cd ../environment.py
git pull origin master

cd ../maze_generator.py
git pull origin master

cd ../place_cell
git pull origin master

cd ../maze_visualizer
git pull origin master
