%global _hardened_build 1

Name:    vala-panel-appmenu
Version: 25.04.0
Release: 1%{?dist}
License: LGPL-3.0+
Summary: This package provides Application Menu plugin for vala-panel
URL:     https://gitlab.com/vala-panel-project/vala-panel-appmenu

Source0: https://gitlab.com/vala-panel-project/vala-panel-appmenu/-/archive/8c8e788bf04c8c2911b72a24e3b79842d5b2b286/vala-panel-appmenu-8c8e788bf04c8c2911b72a24e3b79842d5b2b286.zip

BuildRequires: bamf-daemon
BuildRequires: cmake >= 2.8.0
BuildRequires: gettext
BuildRequires: vala >= 0.32.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires: pkgconfig(libpeas-1.0) >= 1.2.0
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(libwnck-3.0) >= 3.4.0
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)

Provides: vala-panel-appmenu-plugin

Requires: bamf-daemon
Requires: libdbusmenu
Requires: libdbusmenu-gtk2
Requires: libdbusmenu-gtk3
Requires: libappmenu-gtk2-parser
Requires: libappmenu-gtk3-parser
Requires: appmenu-gtk-module-common
Requires: appmenu-gtk2-module
Requires: appmenu-gtk3-module
Requires: appmenu-qt5
Requires: appmenu-qt5ct-profile.d

%description
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.



%package -n xfce4-vala-panel-appmenu-plugin
Summary:    This package provides Application Menu plugin for xfce4-panel
Requires:   bamf-daemon
Requires:   libdbusmenu
Requires:   libdbusmenu-gtk2
Requires:   libdbusmenu-gtk3
Requires:   appmenu-gtk-module-common
Requires:   appmenu-gtk2-module
Requires:   appmenu-gtk3-module
Requires:   appmenu-qt5
Requires:   appmenu-qt5-profile.d
Provides:   vala-panel-appmenu-plugin

%description -n xfce4-vala-panel-appmenu-plugin
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.

%package -n    libappmenu-gtk-parser-devel
Summary:       Common development-files for libappmenu-gtk{2,3}-parser
BuildArch:     noarch
BuildRequires: gtk-doc
Requires:      gtk-doc

%description -n libappmenu-gtk-parser-devel
This package contains common headers and documentation for
libappmenu-gtk{2,3}-parser.


%package -n    libappmenu-gtk2-parser
Summary:       Gtk2MenuShell to GMenuModel parser
BuildRequires: pkgconfig(gtk+-2.0)

%description -n libappmenu-gtk2-parser
This library converts Gtk2MenuShells into GMenuModels.


%package -n libappmenu-gtk2-parser-devel
Summary:    Development-files for libappmenu-gtk2-parser
Requires:   pkgconfig(gtk+-2.0)%{?_isa}
Requires:   libappmenu-gtk-parser-devel == %{version}-%{release}
Requires:   libappmenu-gtk2-parser%{?_isa} == %{version}-%{release}

%description -n libappmenu-gtk2-parser-devel
This package contains development-files for libappmenu-gtk2-parser.


%package -n    libappmenu-gtk3-parser
Summary:       Gtk3MenuShell to GMenuModel parser
BuildRequires: pkgconfig(gtk+-3.0)

%description -n libappmenu-gtk3-parser
This library converts Gtk3MenuShells into GMenuModels.


%package -n libappmenu-gtk3-parser-devel
Summary:    Development-files for libappmenu-gtk3-parser
Requires:   pkgconfig(gtk+-3.0)%{?_isa}
Requires:   libappmenu-gtk-parser-devel == %{version}-%{release}
Requires:   libappmenu-gtk3-parser%{?_isa} == %{version}-%{release}

%description -n libappmenu-gtk3-parser-devel
This package contains development-files for libappmenu-gtk3-parser.


%package -n    appmenu-gtk-module-common
Summary:       Common files for appmenu-gtk{2,3}-module
BuildRequires: systemd

%description -n appmenu-gtk-module-common
This package contains common data-files for appmenu-gtk{2,3}-module.


%package -n appmenu-gtk2-module
Summary:    Gtk2MenuShell D-Bus exporter
Requires:   libappmenu-gtk2-parser%{?_isa} == %{version}-%{release}
Requires:   appmenu-gtk-module-common == %{version}-%{release}
Provides:   appmenu-gtk == %{version}-%{release}
Provides:   appmenu-gtk%{?_isa} == %{version}-%{release}

%description -n appmenu-gtk2-module
This GTK 2 module exports Gtk2MenuShells over D-Bus.


%package -n appmenu-gtk3-module
Summary:    Gtk3MenuShell D-Bus exporter
Requires:   libappmenu-gtk3-parser%{?_isa} == %{version}-%{release}
Requires:   appmenu-gtk-module-common == %{version}-%{release}
Provides:   appmenu-gtk3 == %{version}-%{release}
Provides:   appmenu-gtk3%{?_isa} == %{version}-%{release}


%description -n appmenu-gtk3-module
This GTK 3 module exports Gtk3MenuShells over D-Bus.

%package -n appmenu-qt5ct-profile.d
Summary:    Profile.d-config for appmenu by respecting qt5ct styles
BuildArch:  noarch
Requires:   qt5ct
Requires:   setup

%description -n appmenu-qt5ct-profile.d
This package contains profile.d-config-files for appmenu by respecting qt5ct styles.


%prep
%autosetup -p1

cat > appmenu-gtk-module.sh << EOF
if [ "$XDG_SESSION_DESKTOP" == "budgie-desktop" ] || [ "$XDG_SESSION_DESKTOP" == "mate" ] || [ "$XDG_SESSION_DESKTOP" == "xfce" ]; then
    if [ -z "\$%{nil}GTK_MODULES" ]; then
        export GTK_MODULES="appmenu-gtk-module"
    else
        export GTK_MODULES="\$%{nil}GTK_MODULES:appmenu-gtk-module"
    fi
    if [ -z "\$%{nil}UBUNTU_MENUPROXY" ]; then
        export UBUNTU_MENUPROXY=1
    fi
fi
EOF

cat > appmenu-qt5ct.sh << EOF
export QT_QPA_PLATFORMTHEME=qt5ct
EOF

cat > appmenu-qt5ct.csh << EOF
setenv QT_QPA_PLATFORMTHEME qt5ct
EOF

%build
%cmake -DGSETTINGS_COMPILE=OFF -DENABLE_XFCE=ON -DENABLE_VALAPANEL=OFF \
       -DENABLE_BUDGIE=OFF -DENABLE_MATE=OFF -DENABLE_APPMENU_GTK_MODULE=ON \
       -DMAKE_BOLD_APPNAME=ON -DENABLE_JAYATANA=OFF -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install DESTDIR=%{buildroot}
%{__install} -Dm 0644 appmenu-gtk-module.sh %{buildroot}%{_sysconfdir}/profile.d/appmenu-gtk-module.sh
%{__install} -Dm 0644 appmenu-qt5ct.sh %{buildroot}%{_sysconfdir}/profile.d/appmenu-qt5ct.sh
%{__install} -Dm 0644 appmenu-qt5ct.csh %{buildroot}%{_sysconfdir}/profile.d/appmenu-qt5ct.csh
%find_lang %{name}

%{__mkdir} -p %{buildroot}%{_userunitdir}/default.target.wants
%{_bindir}/ln -s %{_userunitdir}/%{name}.service \
                %{buildroot}%{_userunitdir}/default.target.wants/%{name}.service

%post -n   libappmenu-gtk2-parser -p /sbin/ldconfig
%postun -n libappmenu-gtk2-parser -p /sbin/ldconfig

%post -n   libappmenu-gtk3-parser -p /sbin/ldconfig
%postun -n libappmenu-gtk3-parser -p /sbin/ldconfig

%postun -n appmenu-gtk-module-common
if [ $1 -eq 0 ] ; then
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n appmenu-gtk-module-common
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun -n appmenu-gtk2-module
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache &> /dev/null || :

%post -n appmenu-gtk2-module
if [ $1 -eq 1 ] ; then
    %{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache &> /dev/null || :
fi

%postun -n appmenu-gtk3-module
%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache &> /dev/null || :

%post -n appmenu-gtk3-module
if [ $1 -eq 1 ] ; then
    %{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache &> /dev/null || :
fi

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_userunitdir}/default.target.wants/%{name}.service

%files -n xfce4-vala-panel-appmenu-plugin
%{_libdir}/xfce4/panel/plugins/libappmenu-xfce.so
%{_datadir}/xfce4/panel/plugins/appmenu.desktop

%files -n libappmenu-gtk-parser-devel
%{_includedir}/appmenu-gtk-parser

%files -n libappmenu-gtk2-parser
%license LICENSE*
%{_libdir}/libappmenu-gtk2-parser.so.*

%files -n libappmenu-gtk2-parser-devel
%{_libdir}/libappmenu-gtk2-parser.so
%{_libdir}/pkgconfig/appmenu-gtk2-parser.pc

%files -n libappmenu-gtk3-parser
%license LICENSE
%{_libdir}/libappmenu-gtk3-parser.so.*

%files -n libappmenu-gtk3-parser-devel
%{_libdir}/libappmenu-gtk3-parser.so
%{_libdir}/pkgconfig/appmenu-gtk3-parser.pc

%files -n appmenu-gtk-module-common
%license LICENSE
%config %{_sysconfdir}/profile.d/appmenu-gtk-module.*
%{_libexecdir}/vala-panel/appmenu-registrar
%{_datadir}/dbus-1/services/com.canonical.AppMenu.Registrar.service
%{_datadir}/glib-2.0/schemas/*
%{_userunitdir}/appmenu-gtk-module.service

%files -n appmenu-gtk2-module
%{_libdir}/gtk-2.0/modules/libappmenu-gtk-module.so

%files -n appmenu-gtk3-module
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module.so

%files -n appmenu-qt5ct-profile.d
%{_sysconfdir}/profile.d/appmenu-qt5ct.*

%changelog
* Mon Sep 10 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.7.1-1
- update to 0.7.1

* Thu Aug 30 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.7.0-1
- update to 0.7.0
- update project URL

* Sun Apr 29 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.6.1-3
- rebuild

* Sun Jan 28 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.6.1-2
- force appmenu to use qt5ct as QT_QPA_PLATFORMTHEME
- set -DMAKE_BOLD_APPNAME=ON to make appname menu font bold

* Sun Jan 07 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.6.1-1
- update to 0.6.1

* Wed Jan 03 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.6.0-1
- update to 0.6.0

* Wed Dec 20 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.6-1
- update to 0.5.6

* Fri Dec 01 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.5-1
- update to 0.5.5

* Wed Nov 22 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.4-2
- set GTK_MODULES only on budgie, mate, and xfce session

* Mon Nov 20 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.4-1
- update to 0.5.4

* Sat Nov 04 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.3-2
- rebuild

* Fri Aug 11 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.3-1
- update to 0.5.3

* Sat Jul 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-3
- Fix wrong dependencies name

* Thu Jul 13 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-2
- Don't build budgie plugin

* Thu Jul 13 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-1
- build budgie plugin
- update spec file

* Sun Apr 16 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.4.4-1
- update spec file

* Mon Apr 27 2015 Konstantin <ria.freelander@gmail.com> - 0.4.4
- Generated by CMake UseRPMTools macros

