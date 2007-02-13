%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish_PP
Summary:	Crypt::Blowfish_PP Perl module - pure Perl Blowfish alghoritm implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::Blowfish_PP - implementacja algorytmu Blowfish w samym Perlu
Name:		perl-Crypt-Blowfish_PP
Version:	1.12
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6bf7dc80967eaf3047b67b26b015267d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crypt::Blowfish_PP module provides for users to use the Blowfish
encryption algorithm in Perl. The implementation is entirely Object
Oriented, as there is quite a lot of context inherent in making
Blowfish as fast as it is. The key is anywhere between 64 and 448 bits
(8 and 56 bytes), and should be passed as a packed string. The
transformation itself is a 16-round Feistel Network, and operates on a
64 bit block.

%description -l pl.UTF-8
Moduł Crypt::Blowfish_PP pozwala na korzystanie z algorytmu
szyfrowania Blowfish w samym Perlu. Implementacja jest w pełni
zorientowana obiektowo, jako że potrzeba sporo rzeczy związanych z
kontekstem, aby Blowfish działał tak szybko jak działa. Klucza może
dowolnej długości między 64 a 448 bitów (8 i 56 bajtów) i powinien być
przekazany jako spakowany łańcuch. Sama transformacja jest 16-krokową
siecią Feistela i operuje na 64-bitowym bloku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{perl_vendorlib}/Crypt/Blowfish_PP.pm
%{_mandir}/man3/*
