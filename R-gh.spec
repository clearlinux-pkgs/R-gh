#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gh
Version  : 1.0.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/gh_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gh_1.0.1.tar.gz
Summary  : 'GitHub' 'API'
Group    : Development/Tools
License  : MIT
BuildRequires : R-cli
BuildRequires : R-httr
BuildRequires : R-ini
BuildRequires : R-jsonlite
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
# gh
> GitHub API
[![Linux Build Status](https://travis-ci.org/r-lib/gh.svg?branch=master)](https://travis-ci.org/r-lib/gh)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/r-lib/gh?svg=true)](https://ci.appveyor.com/project/gaborcsardi/gh)
[![](http://www.r-pkg.org/badges/version/gh)](http://www.r-pkg.org/pkg/gh)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/gh)](http://www.r-pkg.org/pkg/gh)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/gh/master.svg)](https://codecov.io/github/r-lib/gh?branch=master)

%prep
%setup -q -c -n gh

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552896717

%install
export SOURCE_DATE_EPOCH=1552896717
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gh
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gh
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gh
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  gh || :


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
/usr/lib64/R/library/gh/NAMESPACE
/usr/lib64/R/library/gh/NEWS.md
/usr/lib64/R/library/gh/R/gh
/usr/lib64/R/library/gh/R/gh.rdb
/usr/lib64/R/library/gh/R/gh.rdx
/usr/lib64/R/library/gh/README.md
/usr/lib64/R/library/gh/help/AnIndex
/usr/lib64/R/library/gh/help/aliases.rds
/usr/lib64/R/library/gh/help/gh.rdb
/usr/lib64/R/library/gh/help/gh.rdx
/usr/lib64/R/library/gh/help/paths.rds
/usr/lib64/R/library/gh/html/00Index.html
/usr/lib64/R/library/gh/html/R.css
/usr/lib64/R/library/gh/tests/testthat.R
/usr/lib64/R/library/gh/tests/testthat/helper-offline.R
/usr/lib64/R/library/gh/tests/testthat/helper.R
/usr/lib64/R/library/gh/tests/testthat/test-build_request.R
/usr/lib64/R/library/gh/tests/testthat/test-github_remote.R
/usr/lib64/R/library/gh/tests/testthat/test-mock-error.R
/usr/lib64/R/library/gh/tests/testthat/test-mock-repos.R
/usr/lib64/R/library/gh/tests/testthat/test-mock-whoami.R
/usr/lib64/R/library/gh/tests/testthat/test-utils.R
