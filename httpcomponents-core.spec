Name:              httpcomponents-core
Summary:           Set of low level Java HTTP transport components for HTTP services
Version:           4.1
Release:           5
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
Patch0:            0001-Remove-unneeded-pom-dependencies.patch
BuildArch:         noarch

BuildRequires:     httpcomponents-project
BuildRequires:     java >= 0:1.6.0
BuildRequires:     jpackage-utils
BuildRequires:     maven-surefire-provider-junit4

Requires:          java >= 0:1.6.0
Requires:          jpackage-utils

Requires(post):    jpackage-utils
Requires(postun):  jpackage-utils

%description
HttpCore is a set of low level HTTP transport components that can be
used to build custom client and server side HTTP services with a
minimal footprint. HttpCore supports two I/O models: blocking I/O
model based on the classic Java I/O and non-blocking, event driven I/O
model based on Java NIO.

The blocking I/O model may be more appropriate for data intensive, low
latency scenarios, whereas the non-blocking model may be more
appropriate for high latency scenarios where raw data throughput is
less important than the ability to handle thousands of simultaneous
HTTP connections in a resource efficient manner.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description    javadoc
%{summary}.


%prep
%setup -q
%patch0 -p1

%build
export maven_repo_local=$(pwd)/.m2/repository
install -d $maven_repo_local

# start using install again when bundle plugin is updated to 2.1.0
mvn-jpp -Dmaven.repo.local=$maven_repo_local \
        package javadoc:aggregate

%install
install -d %{buildroot}/%{_mavenpomdir}
install -d %{buildroot}/%{_javadir}/%{name}

for m in httpcore httpcore-nio httpcore-osgi; do
    # poms
    install -m 0644 $m/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-$m.pom

    # jars - osgi doesn't have one
    if [ -f $m/target/$m-%{version}.jar ];then
        install -m 0644 $m/target/$m-%{version}.jar %{buildroot}%{_javadir}/%{name}/$m.jar
    fi

    %add_to_maven_depmap org.apache.httpcomponents $m %{version} JPP/%{name} $m
done

# parent
install -D -m 0644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_to_maven_depmap org.apache.httpcomponents %{name} %{version} JPP/%{name} %{name}

# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}*.pom
%{_javadir}/%{name}

%files javadoc
%doc LICENSE.txt
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

