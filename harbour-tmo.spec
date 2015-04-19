Name: harbour-tmo
Version: 0.1
Release: 1
Summary: An app for the talk.maemo.org community.
URL: https://github.com/mattaustin/tmo
License: ASL 2.0 and MIT
Source: https://github.com/mattaustin/tmo/archive/0.1.tar.gz
BuildArch: noarch
Requires: libsailfishapp-launcher
Requires: pyotherside-qml-plugin-python3-qt5
Requires: sailfishsilica-qt5


%description
An app for the talk.maemo.org community.


%prep
%setup -q -n tmo-%{version}


%install
rm -rf %{buildroot}

# Application files
TARGET=%{buildroot}/%{_datadir}/%{name}
mkdir -p $TARGET
mkdir -p $TARGET/qml
cp -rpv tmo $TARGET/
cp -Hrpv qml/silica/* $TARGET/qml/
ln -s main.qml $TARGET/qml/%{name}.qml

# Documentation files
# Normally this is automatic using %doc in the %files section below, but it is
# not permitted by harbour, so we're placing with the application files.
TARGET=%{buildroot}/%{_datadir}/%{name}/doc
mkdir -p $TARGET
cp README.rst $TARGET/
cp LICENSE $TARGET/

# Desktop Entry
TARGET=%{buildroot}/%{_datadir}/applications
mkdir -p $TARGET
cp -rpv %{name}.desktop $TARGET/

# Icon
#TARGET=%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/
#mkdir -p $TARGET
#cp -rpv icons/sailfishos.png $TARGET/%{name}.png


%files
#%doc README.rst LICENSE
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
#%{_datadir}/icons/hicolor/*/apps/%{name}.png
