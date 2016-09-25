TMP_DIR=/tmp/npm-install-`date +%s`
mkdir -p $TMP_DIR
(cd $TMP_DIR;
    wget https://nodejs.org/dist/v6.5.0/node-v6.5.0-linux-x64.tar.xz;
    tar -xvf node-*.tar.xz;
    rm *.tar.xz)
cp -r $TMP_DIR/node-* node
for folder in bin lib; do
    echo "ln -s $PWD/$folder/* $folder..."
    ln -s $PWD/node/$folder/* $folder
done
