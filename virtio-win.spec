Name: virtio-win
Version: 0.1
Release: 81.1%{?dist}
Summary: Windows guest drivers
Group: FIXME
License: Unknown
URL: http://www.linux-kvm.org/page/WindowsGuestDrivers
Source0: http://alt.fedoraproject.org/pub/alt/virtio-win/latest/%{name}-%{version}-81.iso
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: xorriso
BuildArch: noarch

%description
Windows guest drivers

%prep
mkdir -p %{_builddir}/%{name}-%{version}
xorriso -osirrox on -indev %{SOURCE0} -extract / %{_builddir}/%{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/amd64
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/i386
cp -r %{_builddir}/%{name}-%{version}/XP/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/WIN7/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2008
cp -r %{_builddir}/%{name}-%{version}/WIN8/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2012
cp -r %{_builddir}/%{name}-%{version}/WIN7/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win7
cp -r %{_builddir}/%{name}-%{version}/WIN8/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win8
cp -r %{_builddir}/%{name}-%{version}/XP/AMD64 %{buildroot}/usr/share/virtio-win/drivers/amd64/WinXP
cp -r %{_builddir}/%{name}-%{version}/XP/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/WIN7/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2008
cp -r %{_builddir}/%{name}-%{version}/WIN8/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2012
cp -r %{_builddir}/%{name}-%{version}/WIN7/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win7
cp -r %{_builddir}/%{name}-%{version}/WIN8/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win8
cp -r %{_builddir}/%{name}-%{version}/XP/X86 %{buildroot}/usr/share/virtio-win/drivers/i386/WinXP

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
/usr/share/virtio-win

%changelog
* Thu Aug 28 2014 zwindler
- Updated paths, version, added win8 and win2012
* Fri May 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-22.1
- Initial package
