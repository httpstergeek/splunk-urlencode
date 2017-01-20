# Splunk-urlencode

Custom Splunk command to urlencode fields. Used to build proper urls from data in splunk. Command replaces fields with encoded versions.

## Getting Started

* Copy or Clone the urlencode directory to $SPLUNK_HOME/etc/apps.
* run urlencode/build/setup.sh  - Will install splunk sdk
* Once installed restart Splunk.

## Usage

 ```
 ... | urlencode fields="<field1>,<field2>,<field3>""
 ```

### Prerequisites

* Splunk 6.x

## Acknowledgments

* https://answers.splunk.com/answers/441031/how-to-encode-a-url-for-a-hipchat-notification-ale.html#answer-440538
