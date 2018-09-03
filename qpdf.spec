#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qpdf
Version  : 8.2.1
Release  : 4
URL      : https://github.com/qpdf/qpdf/releases/download/release-qpdf-8.2.1/qpdf-8.2.1.tar.gz
Source0  : https://github.com/qpdf/qpdf/releases/download/release-qpdf-8.2.1/qpdf-8.2.1.tar.gz
Summary  : PDF transformation library
Group    : Development/Tools
License  : Apache-2.0
Requires: qpdf-bin
Requires: qpdf-lib
Requires: qpdf-license
Requires: qpdf-man
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(zlib)

%description
This directory contains files that I want to keep around because I
hand-created them or otherwise went to some trouble and used them in
some fashion in the test suite. Any file in this directory should be
referenced in a comment in the test code.

%package bin
Summary: bin components for the qpdf package.
Group: Binaries
Requires: qpdf-license
Requires: qpdf-man

%description bin
bin components for the qpdf package.


%package dev
Summary: dev components for the qpdf package.
Group: Development
Requires: qpdf-lib
Requires: qpdf-bin
Provides: qpdf-devel

%description dev
dev components for the qpdf package.


%package doc
Summary: doc components for the qpdf package.
Group: Documentation
Requires: qpdf-man

%description doc
doc components for the qpdf package.


%package lib
Summary: lib components for the qpdf package.
Group: Libraries
Requires: qpdf-license

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
%setup -q -n qpdf-8.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535936936
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1535936936
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qpdf
cp LICENSE.txt %{buildroot}/usr/share/doc/qpdf/LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/include/qpdf/Pipeline.hh
/usr/include/qpdf/Pl_Buffer.hh
/usr/include/qpdf/Pl_Concatenate.hh
/usr/include/qpdf/Pl_Count.hh
/usr/include/qpdf/Pl_DCT.hh
/usr/include/qpdf/Pl_Discard.hh
/usr/include/qpdf/Pl_Flate.hh
/usr/include/qpdf/Pl_QPDFTokenizer.hh
/usr/include/qpdf/Pl_RunLength.hh
/usr/include/qpdf/Pl_StdioFile.hh
/usr/include/qpdf/PointerHolder.hh
/usr/include/qpdf/QPDF.hh
/usr/include/qpdf/QPDFAcroFormDocumentHelper.hh
/usr/include/qpdf/QPDFAnnotationObjectHelper.hh
/usr/include/qpdf/QPDFDocumentHelper.hh
/usr/include/qpdf/QPDFExc.hh
/usr/include/qpdf/QPDFFormFieldObjectHelper.hh
/usr/include/qpdf/QPDFObjGen.hh
/usr/include/qpdf/QPDFObject.hh
/usr/include/qpdf/QPDFObjectHandle.hh
/usr/include/qpdf/QPDFObjectHelper.hh
/usr/include/qpdf/QPDFPageDocumentHelper.hh
/usr/include/qpdf/QPDFPageObjectHelper.hh
/usr/include/qpdf/QPDFSystemError.hh
/usr/include/qpdf/QPDFTokenizer.hh
/usr/include/qpdf/QPDFWriter.hh
/usr/include/qpdf/QPDFXRefEntry.hh
/usr/include/qpdf/QTC.hh
/usr/include/qpdf/QUtil.hh
/usr/include/qpdf/RandomDataProvider.hh
/usr/include/qpdf/Types.h
/usr/include/qpdf/qpdf-c.h
/usr/lib64/libqpdf.so
/usr/lib64/pkgconfig/libqpdf.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/qpdf/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqpdf.so.21
/usr/lib64/libqpdf.so.21.2.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/qpdf/LICENSE.txt

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/fix-qdf.1
/usr/share/man/man1/qpdf.1
/usr/share/man/man1/zlib-flate.1
