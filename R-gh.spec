#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gh
Version  : 1.3.1
Release  : 41
URL      : https://cran.r-project.org/src/contrib/gh_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gh_1.3.1.tar.gz
Summary  : 'GitHub' 'API'
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-gitcreds
Requires: R-httr
Requires: R-ini
Requires: R-jsonlite
BuildRequires : R-cli
BuildRequires : R-gitcreds
BuildRequires : R-httr
BuildRequires : R-ini
BuildRequires : R-jsonlite
BuildRequires : R-mockery
BuildRequires : buildreq-R

%description
# gh
<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/gh/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/gh/actions)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/gh/branch/main/graph/badge.svg)](https://app.codecov.io/gh/r-lib/gh?branch=main)
[![](https://www.r-pkg.org/badges/version/gh)](https://www.r-pkg.org/pkg/gh)
[![CRAN RStudio mirror
downloads](https://cranlogs.r-pkg.org/badges/gh)](https://www.r-pkg.org/pkg/gh)
[![R-CMD-check](https://github.com/r-lib/gh/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/gh/actions/workflows/R-CMD-check.yaml)
<!-- badges: end -->

%prep
%setup -q -n gh
cd %{_builddir}/gh

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662658949

%install
export SOURCE_DATE_EPOCH=1662658949
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gh/DESCRIPTION
/usr/lib64/R/library/gh/INDEX
/usr/lib64/R/library/gh/LICENSE
/usr/lib64/R/library/gh/Meta/Rd.rds
/usr/lib64/R/library/gh/Meta/features.rds
/usr/lib64/R/library/gh/Meta/hsearch.rds
/usr/lib64/R/library/gh/Meta/links.rds
/usr/lib64/R/library/gh/Meta/nsInfo.rds
/usr/lib64/R/library/gh/Meta/package.rds
/usr/lib64/R/library/gh/Meta/vignette.rds
/usr/lib64/R/library/gh/NAMESPACE
/usr/lib64/R/library/gh/NEWS.md
/usr/lib64/R/library/gh/R/gh
/usr/lib64/R/library/gh/R/gh.rdb
/usr/lib64/R/library/gh/R/gh.rdx
/usr/lib64/R/library/gh/WORDLIST
/usr/lib64/R/library/gh/doc/index.html
/usr/lib64/R/library/gh/doc/managing-personal-access-tokens.R
/usr/lib64/R/library/gh/doc/managing-personal-access-tokens.Rmd
/usr/lib64/R/library/gh/doc/managing-personal-access-tokens.html
/usr/lib64/R/library/gh/help/AnIndex
/usr/lib64/R/library/gh/help/aliases.rds
/usr/lib64/R/library/gh/help/gh.rdb
/usr/lib64/R/library/gh/help/gh.rdx
/usr/lib64/R/library/gh/help/paths.rds
/usr/lib64/R/library/gh/html/00Index.html
/usr/lib64/R/library/gh/html/R.css
/usr/lib64/R/library/gh/tests/testthat.R
/usr/lib64/R/library/gh/tests/testthat/_snaps/gh_request.md
/usr/lib64/R/library/gh/tests/testthat/helper-offline.R
/usr/lib64/R/library/gh/tests/testthat/helper.R
/usr/lib64/R/library/gh/tests/testthat/test-errors.R
/usr/lib64/R/library/gh/tests/testthat/test-gh.R
/usr/lib64/R/library/gh/tests/testthat/test-gh_rate_limit.R
/usr/lib64/R/library/gh/tests/testthat/test-gh_request.R
/usr/lib64/R/library/gh/tests/testthat/test-gh_token.R
/usr/lib64/R/library/gh/tests/testthat/test-gh_whoami.R
/usr/lib64/R/library/gh/tests/testthat/test-git.R
/usr/lib64/R/library/gh/tests/testthat/test-mock-repos.R
/usr/lib64/R/library/gh/tests/testthat/test-old-templates.R
/usr/lib64/R/library/gh/tests/testthat/test-spelling.R
/usr/lib64/R/library/gh/tests/testthat/test-utils.R
