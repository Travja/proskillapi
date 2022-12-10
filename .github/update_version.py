import re


def replace_version():
    regex = r'<artifactId>proskillapi<\/artifactId>\n^[ ]{4}<version>((\d.)+)(-SNAPSHOT)?<\/version>$'
    with open('pom.xml', 'r') as pom:
        contents = pom.read()
        ver = re.findall(regex, contents, re.MULTILINE)
        version = ver[0][0]
        patch = int(ver[0][1])
        new_version = version.replace(ver[0][1], str(patch + 1))
        print(new_version)
        contents = re.sub(regex,
                          '<artifactId>proskillapi</artifactId>\n    <version>' + new_version + '</version>',
                          contents,
                          1,
                          re.MULTILINE)
    with open('pom.xml', 'w') as pom:
        pom.write(contents)


replace_version()
