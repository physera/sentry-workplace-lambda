# Sentry integration for Facebook Workplace via AWS Lambda

This repository contains an [AWS Lambda](https://aws.amazon.com/lambda/) function which will post [Sentry](https://sentry.io) updates to a [Facebook Workplace](https://workplace.facebook.com) group of your choosing.
For an overview of the approach, see [this document](https://github.com/physera/workplace-lambda).

## Setup

To make this work, first follow the instructions [here](https://github.com/physera/workplace-lambda#setup). Then you'll need to set things up on Sentry.

### Set up callbacks on Sentry

We now just need to make sure Sentry calls your endpoint whenever something happens.

* From the Sentry project you want to monitor, go to Settings ... Alerts.
* Select `Webhooks` from the list of Integrations at the bottom.
* Paste in the URL for the API Gateway trigger into the `Callback URLs` field.

## Version History

* 2018-06-19 Initial release
