#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0x8A75D10998012C7E (ejb@ql.org)
#
Name     : qpdf
Version  : 11.9.1
Release  : 13
URL      : https://github.com/qpdf/qpdf/releases/download/v11.9.1/qpdf-11.9.1.tar.gz
Source0  : https://github.com/qpdf/qpdf/releases/download/v11.9.1/qpdf-11.9.1.tar.gz
Source1  : https://github.com/qpdf/qpdf/releases/download/v11.9.1/qpdf-11.9.1.tar.gz.asc
Source2  : 8A75D10998012C7E.pkey
Summary  : PDF transformation library
Group    : Development/Tools
License  : Apache-2.0
Requires: qpdf-bin = %{version}-%{release}
Requires: qpdf-lib = %{version}-%{release}
Requires: qpdf-license = %{version}-%{release}
Requires: qpdf-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gnupg
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains files that I want to keep around because I
hand-created them or otherwise went to some trouble and used them in
some fashion in the test suite. Any file in this directory should be
referenced in a comment in the test code.

%package bin
Summary: bin components for the qpdf package.
Group: Binaries
Requires: qpdf-license = %{version}-%{release}

%description bin
bin components for the qpdf package.


%package dev
Summary: dev components for the qpdf package.
Group: Development
Requires: qpdf-lib = %{version}-%{release}
Requires: qpdf-bin = %{version}-%{release}
Provides: qpdf-devel = %{version}-%{release}
Requires: qpdf = %{version}-%{release}

%description dev
dev components for the qpdf package.


%package doc
Summary: doc components for the qpdf package.
Group: Documentation
Requires: qpdf-man = %{version}-%{release}

%description doc
doc components for the qpdf package.


%package lib
Summary: lib components for the qpdf package.
Group: Libraries
Requires: qpdf-license = %{version}-%{release}

%description lib
lib components for the qpdf package.


%package license
Summary: license components for the qpdf package.
Group: Default

%description license
license components for the qpdf package.


%package man
Summary: man components for the qpdf package.
Group: Default

%description man
man components for the qpdf package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 8A75D10998012C7E' gpg.status
%setup -q -n qpdf-11.9.1
cd %{_builddir}/qpdf-11.9.1
pushd ..
cp -a qpdf-11.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720047127
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../buildavx2/clr-build-avx2;
make test || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720047127
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qpdf
cp %{_builddir}/qpdf-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/qpdf/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/fix-qdf
/V3/usr/bin/qpdf
/V3/usr/bin/zlib-flate
/usr/bin/fix-qdf
/usr/bin/qpdf
/usr/bin/zlib-flate

%files dev
%defattr(-,root,root,-)
/usr/include/qpdf/Buffer.hh
/usr/include/qpdf/BufferInputSource.hh
/usr/include/qpdf/ClosedFileInputSource.hh
/usr/include/qpdf/Constants.h
/usr/include/qpdf/DLL.h
/usr/include/qpdf/FileInputSource.hh
/usr/include/qpdf/InputSource.hh
/usr/include/qpdf/JSON.hh
/usr/include/qpdf/PDFVersion.hh
/usr/include/qpdf/Pipeline.hh
/usr/include/qpdf/Pl_Buffer.hh
/usr/include/qpdf/Pl_Concatenate.hh
/usr/include/qpdf/Pl_Count.hh
/usr/include/qpdf/Pl_DCT.hh
/usr/include/qpdf/Pl_Discard.hh
/usr/include/qpdf/Pl_Flate.hh
/usr/include/qpdf/Pl_Function.hh
/usr/include/qpdf/Pl_OStream.hh
/usr/include/qpdf/Pl_QPDFTokenizer.hh
/usr/include/qpdf/Pl_RunLength.hh
/usr/include/qpdf/Pl_StdioFile.hh
/usr/include/qpdf/Pl_String.hh
/usr/include/qpdf/PointerHolder.hh
/usr/include/qpdf/QIntC.hh
/usr/include/qpdf/QPDF.hh
/usr/include/qpdf/QPDFAcroFormDocumentHelper.hh
/usr/include/qpdf/QPDFAnnotationObjectHelper.hh
/usr/include/qpdf/QPDFCryptoImpl.hh
/usr/include/qpdf/QPDFCryptoProvider.hh
/usr/include/qpdf/QPDFDocumentHelper.hh
/usr/include/qpdf/QPDFEFStreamObjectHelper.hh
/usr/include/qpdf/QPDFEmbeddedFileDocumentHelper.hh
/usr/include/qpdf/QPDFExc.hh
/usr/include/qpdf/QPDFFileSpecObjectHelper.hh
/usr/include/qpdf/QPDFFormFieldObjectHelper.hh
/usr/include/qpdf/QPDFJob.hh
/usr/include/qpdf/QPDFLogger.hh
/usr/include/qpdf/QPDFMatrix.hh
/usr/include/qpdf/QPDFNameTreeObjectHelper.hh
/usr/include/qpdf/QPDFNumberTreeObjectHelper.hh
/usr/include/qpdf/QPDFObjGen.hh
/usr/include/qpdf/QPDFObject.hh
/usr/include/qpdf/QPDFObjectHandle.hh
/usr/include/qpdf/QPDFObjectHelper.hh
/usr/include/qpdf/QPDFOutlineDocumentHelper.hh
/usr/include/qpdf/QPDFOutlineObjectHelper.hh
/usr/include/qpdf/QPDFPageDocumentHelper.hh
/usr/include/qpdf/QPDFPageLabelDocumentHelper.hh
/usr/include/qpdf/QPDFPageObjectHelper.hh
/usr/include/qpdf/QPDFStreamFilter.hh
/usr/include/qpdf/QPDFSystemError.hh
/usr/include/qpdf/QPDFTokenizer.hh
/usr/include/qpdf/QPDFUsage.hh
/usr/include/qpdf/QPDFWriter.hh
/usr/include/qpdf/QPDFXRefEntry.hh
/usr/include/qpdf/QTC.hh
/usr/include/qpdf/QUtil.hh
/usr/include/qpdf/RandomDataProvider.hh
/usr/include/qpdf/Types.h
/usr/include/qpdf/auto_job_c_att.hh
/usr/include/qpdf/auto_job_c_copy_att.hh
/usr/include/qpdf/auto_job_c_enc.hh
/usr/include/qpdf/auto_job_c_main.hh
/usr/include/qpdf/auto_job_c_pages.hh
/usr/include/qpdf/auto_job_c_set_page_labels.hh
/usr/include/qpdf/auto_job_c_uo.hh
/usr/include/qpdf/qpdf-c.h
/usr/include/qpdf/qpdfjob-c.h
/usr/include/qpdf/qpdflogger-c.h
/usr/lib64/cmake/qpdf/libqpdfTargets-relwithdebinfo.cmake
/usr/lib64/cmake/qpdf/libqpdfTargets.cmake
/usr/lib64/cmake/qpdf/qpdfConfig.cmake
/usr/lib64/cmake/qpdf/qpdfConfigVersion.cmake
/usr/lib64/libqpdf.so
/usr/lib64/pkgconfig/libqpdf.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/qpdf/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libqpdf.so.29.9.1
/usr/lib64/libqpdf.so.29
/usr/lib64/libqpdf.so.29.9.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qpdf/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fix-qdf.1
/usr/share/man/man1/qpdf.1
/usr/share/man/man1/zlib-flate.1
