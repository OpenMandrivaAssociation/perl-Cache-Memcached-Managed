%define upstream_name    Cache-Memcached-Managed
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.24
Release:	3

Summary:	Inactive Cache::Memcache::Managed object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Cache/Cache-Memcached-Managed-0.24.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::Memcached)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	memcached
BuildArch:	noarch

%description
Provides the same API as the Cache::Memcached::Managed manpage, but applies
all methods called to all of the objects specified, except for the new
manpage and the objects manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGELOG META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.200.0-3mdv2011.0
+ Revision: 654246
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 624986
- Add a memcached as a build requires
- import perl-Cache-Memcached-Managed


