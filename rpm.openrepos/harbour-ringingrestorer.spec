# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-ringingrestorer

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    RingingRestorer
Version:    1.4
Release:    1
Group:      Qt/Qt
License:    GPLv3
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-ringingrestorer.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dsme)
BuildRequires:  pkgconfig(mce) >= 1.12.3
BuildRequires:  desktop-file-utils

%description
When changing to silent profile, RingingRestorer will display a dialog where you can quickly set when to restore ringing again.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%pre
# >> pre
su nemo -c "systemctl --user stop %{name}"
exit 0
# << pre

%preun
# >> preun
su nemo -c "systemctl --user stop %{name}"
su nemo -c "systemctl --user disable %{name}"
# << preun

%post
# >> post
su nemo -c "systemctl --user daemon-reload"
su nemo -c "systemctl --user enable %{name}"
su nemo -c "systemctl --user start %{name}"
# << post

%postun
# >> postun
su nemo -c "systemctl --user daemon-reload"
# << postun

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_libdir}/systemd/user/%{name}.service
# >> files
# << files
