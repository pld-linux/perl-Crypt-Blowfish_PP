%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish_PP
Summary:	Crypt::Blowfish_PP Perl module - pure Perl Blowfish alghoritm implementation
Summary(pl):	Modu� Perla Crypt::Blowfish_PP - implementacja algorytmu Blowfish w samym Perlu
Name:		perl-Crypt-Blowfish_PP
Version:	1.12
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu� Crypt::Blowfish_PP pozwala na korzystanie z algorytmu
szyfrowania Blowfish w samym Perlu. Implementacja jest w pe�ni
zorientowana obiektowo, jako �e potrzeba sporo rzeczy zwi�zanych z
kontekstem, aby Blowfish dzia�a� tak szybko jak dzia�a. Klucza mo�e
dowolnej d�ugo�ci mi�dzy 64 a 448 bit�w (8 i 56 bajt�w) i powinien by�
przekazany jako spakowany �a�cuch. Sama transformacja jest 16-krokow�
sieci� Feistela i operuje na 64-bitowym bloku.

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
