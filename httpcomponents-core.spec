
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		httpcomponents-core
Version:	4.2.4
Release:	5.1
License:	GPLv3+
Source0:	httpcomponents-core-4.2.4-5.1-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/httpcomponents-core
BuildArch:	noarch
Summary:	httpcomponents-core bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1.5
Requires:	jpackage-utils
Provides:	httpcomponents-core = 4.2.4-5.1:2014.0
Provides:	mvn(org.apache.httpcomponents:httpcomponents-core) = 4.2.4
Provides:	mvn(org.apache.httpcomponents:httpcomponents-core:pom:) = 4.2.4
Provides:	mvn(org.apache.httpcomponents:httpcore) = 4.2.4
Provides:	mvn(org.apache.httpcomponents:httpcore-nio) = 4.2.4
Provides:	osgi(org.apache.httpcomponents.httpcore) = 4.2.4
Provides:	osgi(org.apache.httpcomponents.httpcore-nio) = 4.2.4

%description
httpcomponents-core bootstrap version.

%files
/usr/share/doc/httpcomponents-core
/usr/share/doc/httpcomponents-core/LICENSE.txt
/usr/share/doc/httpcomponents-core/NOTICE.txt
/usr/share/doc/httpcomponents-core/README.txt
/usr/share/doc/httpcomponents-core/RELEASE_NOTES.txt
/usr/share/java/httpcomponents
/usr/share/java/httpcomponents/httpcore-nio.jar
/usr/share/java/httpcomponents/httpcore.jar
/usr/share/maven-effective-poms/JPP.httpcomponents-httpcore-nio.pom
/usr/share/maven-effective-poms/JPP.httpcomponents-httpcore.pom
/usr/share/maven-fragments/httpcomponents-core.xml
/usr/share/maven-poms/JPP.httpcomponents-httpcomponents-core.pom
/usr/share/maven-poms/JPP.httpcomponents-httpcore-nio.pom
/usr/share/maven-poms/JPP.httpcomponents-httpcore.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
