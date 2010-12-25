%define upstream_name    Cache-Memcached-Managed
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Inactive Cache::Memcache::Managed object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cache::Memcached)
BuildRequires: perl(Scalar::Util)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Provides the same API as the Cache::Memcached::Managed manpage, but applies
all methods called to all of the objects specified, except for the new
manpage and the objects manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGELOG META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


