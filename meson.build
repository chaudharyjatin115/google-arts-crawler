project(
  'arts-crawler',
  version: '1.0.0',
  meson_version: '>=0.60.0'
)

python = import('python').find_installation()

prefix = get_option('prefix')
datadir = get_option('datadir')
bindir = get_option('bindir')

# install the python app files together
install_data(
  ['app.py', 'crawler.py'],
  install_dir: join_paths(prefix, 'lib', 'arts-crawler')
)

# install launcher into /usr/bin
install_symlink(
  'arts-crawler',
  pointing_to: join_paths(prefix, 'lib', 'arts-crawler', 'app.py'),
  install_dir: bindir
)

# desktop file
install_data(
  'data/org.example.ArtsCrawler.desktop',
  install_dir: join_paths(datadir, 'applications')
)

# icon
install_data(
  'data/org.example.ArtsCrawler.svg',
  install_dir: join_paths(datadir, 'icons/hicolor/scalable/apps')
)

# metainfo
install_data(
  'data/org.example.ArtsCrawler.metainfo.xml',
  install_dir: join_paths(datadir, 'metainfo')
)

