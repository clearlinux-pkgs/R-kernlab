#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-kernlab
Version  : 0.9.27
Release  : 22
URL      : https://cran.r-project.org/src/contrib/kernlab_0.9-27.tar.gz
Source0  : https://cran.r-project.org/src/contrib/kernlab_0.9-27.tar.gz
Summary  : Kernel-Based Machine Learning Lab
Group    : Development/Tools
License  : GPL-2.0
Requires: R-kernlab-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
regression, clustering, novelty detection, quantile regression
        and dimensionality reduction.  Among other methods 'kernlab'
        includes Support Vector Machines, Spectral Clustering, Kernel
        PCA, Gaussian Processes and a QP solver.

%package lib
Summary: lib components for the R-kernlab package.
Group: Libraries

%description lib
lib components for the R-kernlab package.


%prep
%setup -q -c -n kernlab

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552925896

%install
export SOURCE_DATE_EPOCH=1552925896
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kernlab
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kernlab
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kernlab
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  kernlab || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/kernlab/CITATION
/usr/lib64/R/library/kernlab/COPYRIGHTS
/usr/lib64/R/library/kernlab/DESCRIPTION
/usr/lib64/R/library/kernlab/INDEX
/usr/lib64/R/library/kernlab/Meta/Rd.rds
/usr/lib64/R/library/kernlab/Meta/data.rds
/usr/lib64/R/library/kernlab/Meta/features.rds
/usr/lib64/R/library/kernlab/Meta/hsearch.rds
/usr/lib64/R/library/kernlab/Meta/links.rds
/usr/lib64/R/library/kernlab/Meta/nsInfo.rds
/usr/lib64/R/library/kernlab/Meta/package.rds
/usr/lib64/R/library/kernlab/Meta/vignette.rds
/usr/lib64/R/library/kernlab/NAMESPACE
/usr/lib64/R/library/kernlab/R/kernlab
/usr/lib64/R/library/kernlab/R/kernlab.rdb
/usr/lib64/R/library/kernlab/R/kernlab.rdx
/usr/lib64/R/library/kernlab/data/income.rda
/usr/lib64/R/library/kernlab/data/musk.rda
/usr/lib64/R/library/kernlab/data/promotergene.rda
/usr/lib64/R/library/kernlab/data/reuters.rda
/usr/lib64/R/library/kernlab/data/spam.rda
/usr/lib64/R/library/kernlab/data/spirals.rda
/usr/lib64/R/library/kernlab/data/ticdata.rda
/usr/lib64/R/library/kernlab/doc/index.html
/usr/lib64/R/library/kernlab/doc/kernlab.R
/usr/lib64/R/library/kernlab/doc/kernlab.Rnw
/usr/lib64/R/library/kernlab/doc/kernlab.pdf
/usr/lib64/R/library/kernlab/help/AnIndex
/usr/lib64/R/library/kernlab/help/aliases.rds
/usr/lib64/R/library/kernlab/help/kernlab.rdb
/usr/lib64/R/library/kernlab/help/kernlab.rdx
/usr/lib64/R/library/kernlab/help/paths.rds
/usr/lib64/R/library/kernlab/html/00Index.html
/usr/lib64/R/library/kernlab/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/kernlab/libs/kernlab.so
/usr/lib64/R/library/kernlab/libs/kernlab.so.avx2
/usr/lib64/R/library/kernlab/libs/kernlab.so.avx512
