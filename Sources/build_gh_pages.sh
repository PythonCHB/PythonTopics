#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../../PythonTopics_gh_pages/

cd ../../PythonTopics_gh_pages
git add * # in case there are new files added
git commit -a
git push
