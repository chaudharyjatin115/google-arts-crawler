pkgname=arts-crawler
pkgver=1.0.0
pkgrel=4
pkgdesc="Download high resolution images from Google Arts & Culture"
arch=('any')
url="https://github.com/chaudharyjatin115/google-arts-crawler"
license=('MIT')

depends=(
  'python'
  'python-numpy'
  'python-pillow'
  'python-click'
  'python-pyperclip'
  'python-pysocks'
  'python-slugify'
  'python-urllib3'
  'python-gobject'
  'gtk4'
  'libadwaita'
  'chromium'
)

makedepends=('meson' 'ninja')

# no source because we build from working tree
source=()
sha256sums=()

build() {
  cd "$startdir"

  meson setup build \
    --prefix=/usr \
    --libdir=lib

  meson compile -C build
}

package() {
  cd "$startdir"
  meson install -C build --destdir="$pkgdir"
}

