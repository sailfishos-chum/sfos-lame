# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       lame

# >> macros
# << macros
%define sover 0

Summary:    The LAME MP3 encoder
Version:    3.100
Release:    0
Group:      Applications/Multimedia
License:    LGPL-2.0-or-later
URL:        https://lame.sourceforge.net/
Source0:    http://prdownloads.sourceforge.net/lame/lame-%{version}.tar.gz
Source1:    lame-rpmlintrc
Source2:    baselibs.conf
Patch0:     lame-field-width-fix.patch
Requires:   libmp3lame%{sover} >= %{version}
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  nasm

%description
LAME is an educational tool to be used for learning about MP3 encoding.
The goal of the LAME project is to use the open source model to improve the
psycho acoustics, noise shaping and speed of MP3.
Another goal of the LAME project is to use these improvements for the basis of
a patent free audio compression codec for the GNU project.

%if "%{?vendor}" == "chum"
Title: LAME
Type: console-application
PackagedBy: nephros
Categories:
 - Multimedia
 - Sound
PackageIcon: https://sourceforge.net/p/lame/svn/HEAD/tree/trunk/logo/logofull.svg?format=raw
Links:
  Homepage: %{url}
  Bugtracker: https://sourceforge.net/p/lame/_list/tickets
%endif


%package doc
Summary:    Documentation for the LAME MP3 encoder
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description doc
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.


%package -n libmp3lame%{sover}
Summary:    The LAME MP3 encoder library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libmp3lame%{sover}
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.


%package -n libmp3lame-devel
Summary:    Development files for the LAME MP3 encoder
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libmp3lame%{sover} = %{version}

%description -n libmp3lame-devel
Contains the header files for use with LAMEs encoding library.

%package mp3rtp
Summary:    MP3 Encoder for RTP Streaming
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}
Requires:   libmp3lame%{sover} >= %{version}

%description mp3rtp
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.

This package includes "mp3rtp", an MP3 encoder with RTP streaming of the output.

%if "%{?vendor}" == "chum"
Title: Lame mp3rtp
Type: console-application
PackagedBy: nephros
Categories:
 - Multimedia
 - Sound
PackageIcon: https://sourceforge.net/p/lame/svn/HEAD/tree/trunk/logo/logofull.svg?format=raw
Links:
  Homepage: %{url}
  Bugtracker: https://sourceforge.net/p/lame/_list/tickets
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# lame-field-width-fix.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
LIBS="-lm" \
CFLAGS="%{optflags}" \
%configure \
--enable-nasm \
--enable-decoder \
--disable-debug \
--enable-mp3rtp \
--with-fileio=lame \
--enable-dynamic-frontends \
--disable-rpath \
--disable-static

%make_build pkgdocdir=%{_defaultdocdir}/%{name}/

# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
make install pkgdocdir=%{_defaultdocdir}/%{name}/ DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libmp3lame.la

#make package config file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/lame.pc
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/lame

Name:           lame
Description: encoder that converts audio to the MP3 file format.
Version:        %{version}
Libs: -L\${libdir} -lmp3lame
Cflags: -I\${includedir}
EOF
pushd %{buildroot}%{_libdir}/pkgconfig/
ln -s lame.pc libmp3lame.pc
popd

for f in ChangeLog README TODO USAGE; do
install -m0644 "$f" "%{buildroot}%{_defaultdocdir}/%{name}/"
done

# << install post

%check
# >> check
%make_build test
# << check

%post -n libmp3lame%{sover} -p /sbin/ldconfig

%postun -n libmp3lame%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/lame
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/lame.1%{?ext_man}
%{_defaultdocdir}/%{name}
# >> files doc
# << files doc

%files -n libmp3lame%{sover}
%defattr(-,root,root,-)
%license COPYING LICENSE
%{_libdir}/libmp3lame.so.%{sover}
%{_libdir}/libmp3lame.so.%{sover}.*
# >> files libmp3lame%{sover}
# << files libmp3lame%{sover}

%files -n libmp3lame-devel
%defattr(-,root,root,-)
%doc API HACKING STYLEGUIDE
%{_includedir}/lame/
%{_libdir}/libmp3lame.so
%{_libdir}/pkgconfig/*pc
# >> files libmp3lame-devel
# << files libmp3lame-devel

%files mp3rtp
%defattr(-,root,root,-)
%{_bindir}/mp3rtp
# >> files mp3rtp
# << files mp3rtp
