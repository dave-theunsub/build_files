Name: thunar-sendto-shredder
Version: 0.01
Release: 1.fc
Summary: Extension for Thunar to more securely erase files and directories
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://dave-theunsub.github.io/thunar-sendto-shredder/

Source: https://bitbucket.org/dave_theunsub/thunar-sendto-shredder/downloads/thunar-sendto-shredder-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: Thunar, coreutils
Requires: perl-Gtk3, perl-Locale-gettext, perl-libwww-perl

%description
A simple extension to add an easy way to securely erase files or directories
using XFCE's Thunar file manager.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/%{perl_vendorlib}/Shredder/
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}/
mkdir -p %{buildroot}/%{_datadir}/pixmaps/

# The main executable
install -p -D -m0755 %{name}  %{buildroot}/%{_bindir}/%{name}

# Images
install -p -D -m0644 images/*.png %{buildroot}/%{_datadir}/pixmaps/

# Man pages
install -p -D -m0644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

# Desktop file(s)
install -p -D -m0644 %{name}.desktop %{buildroot}/%{_datadir}/Thunar/sendto/%{name}.desktop
install -p -D -m0644 %{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Perl files
install -p -m0644 Shredder/*.pm %{buildroot}/%{perl_vendorlib}/Shredder/

desktop-file-install --vendor   ""                      \
        --dir %{buildroot}/%{_datadir}/applications     \
        --delete-original                               \
        --add-category=Utility                          \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc CHANGES DISCLAIMER README.md
%license LICENSE

# The main executable
%{_bindir}/%{name}

# Main Perl libraries
%{perl_vendorlib}/Shredder/

# Image(s)
%{_datadir}/pixmaps/*.png

# Desktop file(s)
%{_datadir}/Thunar/sendto/*.desktop
%{_datadir}/applications/*.desktop

# Man pages
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Oct 28 2016 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release, version 0.01.
