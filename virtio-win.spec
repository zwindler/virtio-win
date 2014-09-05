Name: virtio-win
Version: 0.1
Release: 81.1%{?dist}
Summary: Windows guest drivers
Group: FIXME
License: Unknown
URL: http://www.linux-kvm.org/page/WindowsGuestDrivers
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Windows guest drivers

%prep
mkdir -p %{_builddir}/%{name}-%{version}
mount -o loop /tmp/%{name}.iso /mnt
cp -dpR /mnt/* %{_builddir}/%{name}-%{version}
umount /mnt

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/amd64
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/i386
cp -r %{_builddir}/%{name}-%{version}/wxp/x86 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/xp/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2008
cp -r %{_builddir}/%{name}-%{version}/win8/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2012
cp -r %{_builddir}/%{name}-%{version}/win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win7
cp -r %{_builddir}/%{name}-%{version}/win8/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win8
cp -r %{_builddir}/%{name}-%{version}/wxp/x86 %{buildroot}/usr/share/virtio-win/drivers/amd64/Winxp
cp -r %{_builddir}/%{name}-%{version}/xp/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Winxp
cp -r %{_builddir}/%{name}-%{version}/wxp/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/xp/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/win7/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2008
cp -r %{_builddir}/%{name}-%{version}/win8/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win2012
cp -r %{_builddir}/%{name}-%{version}/win7/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win7
cp -r %{_builddir}/%{name}-%{version}/win8/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Win8
cp -r %{_builddir}/%{name}-%{version}/wxp/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Winxp
cp -r %{_builddir}/%{name}-%{version}/xp/x86 %{buildroot}/usr/share/virtio-win/drivers/i386/Winxp

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
/usr/share/virtio-win

%changelog
* Fri Sep 05 2014 zwindler
- Missing 2003/XP drivers (VIRTIO block!!!) because they were in another directory in ISO file
* Thu Aug 28 2014 zwindler
- Changed again, because xorriso uppercase filenames breaks everything
    now it looks a lot more like NeovaHealth/virtio-win fork from fasrc/virtio-win...
* Thu Aug 28 2014 zwindler
- Updated paths, version, added win8 and win2012
* Fri May 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-22.1
- Initial package
