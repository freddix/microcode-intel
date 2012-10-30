Summary:	Intel CPU Microcode
Name:		microcode-intel
Version:	20120606
Release:	1
License:	GPL
Group:		Base
Source0:	http://downloadmirror.intel.com/21385/eng/microcode-%{version}.tgz
# Source0-md5:	f1e57224265ff498971f50fe6824ba0a
Source1:	intel-microcode2ucode.c
Source2:	LICENSE
URL:		http://www.urbanmyth.org/microcode/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode update files for Intel CPUs.

%prep
%setup -qc

install %{SOURCE2} .

%build
%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -Wall \
	%{SOURCE1} -o intel-microcode2ucode

./intel-microcode2ucode microcode.dat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/intel-ucode
cp intel-ucode/* $RPM_BUILD_ROOT/lib/firmware/intel-ucode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(640,root,root) /lib/firmware/intel-ucode

