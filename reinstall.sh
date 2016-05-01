cd $(dirname $0)

pip3 uninstall -y beautifyMusic
python3 setup.py sdist && pip3 install --user dist/beautifyMusic-0.1.tar.gz
