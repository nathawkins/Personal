mkdir project_directory
cd project_directory/
touch README.md
touch requirements.txt
touch CITATION
touch LICENSE
mkdir data
mkdir doc
mkdir bin
mkdir src
mkdir results

for file in */
do
    cd $file
    touch README.md
    cd ..
done

