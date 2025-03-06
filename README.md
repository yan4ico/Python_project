![Async Logo](https://raw.githubusercontent.com/caolan/async/master/logo/async-logo_readme.jpg)

[![Build Status via Travis CI](https://travis-ci.org/caolan/async.svg?branch=master)](https://travis-ci.org/caolan/async)
[![Build Status via Azure Pipelines](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master)
[![NPM version](https://img.shields.io/npm/v/async.svg)](https://www.npmjs.com/package/async)
[![Coverage Status](https://coveralls.io/repos/caolan/async/badge.svg?branch=master)](https://coveralls.io/r/caolan/async?branch=master)
[![Join the chat at https://gitter.im/caolan/async](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/caolan/async?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![jsDelivr Hits](https://data.jsdelivr.com/v1/package/npm/async/badge?style=rounded)](https://www.jsdelivr.com/package/npm/async)

<!--
|Linux|Windows|MacOS|
|-|-|-|
|[![Linux Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=Linux&configuration=Linux%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master) | [![Windows Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=Windows&configuration=Windows%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master) | [![MacOS Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=OSX&configuration=OSX%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master)| -->

Async is a utility module which provides straight-forward, powerful functions for working with [asynchronous JavaScript](http://caolan.github.io/async/v3/global.html). Although originally designed for use with [Node.js](https://nodejs.org/) and installable via `npm i async`, it can also be used directly in the browser.  A ESM/MJS version is included in the main `async` package that should automatically be used with compatible bundlers such as Webpack and Rollup.

A pure ESM version of Async is available as [`async-es`](https://www.npmjs.com/package/async-es).

For Documentation, visit <https://caolan.github.io/async/>

*For Async v1.5.x documentation, go [HERE](https://github.com/caolan/async/blob/v1.5.2/README.md)*


```javascript
// for use with Node-style callbacks...
var async = require("async");

var obj = {dev: "/dev.json", test: "/test.json", prod: "/prod.json"};
var configs = {};

async.forEachOf(obj, (value, key, callback) => {
    fs.readFile(__dirname + value, "utf8", (err, data) => {
        if (err) return callback(err);
        try {
            configs[key] = JSON.parse(data);
        } catch (e) {
            return callback(e);
        }
        callback();
    });
}, err => {
    if (err) console.error(err.message);
    // configs is now a map of JSON data
    doSomethingWith(configs);
});
```

```javascript
var async = require("async");

// ...or ES2017 async functions
async.mapLimit(urls, 5, async function(url) {
    const response = await fetch(url)
    return response.body
}, (err, results) => {
    if (err) throw err
    // results is now an array of the response bodies
    console.log(results)
})
```

Auto-commit on 2025-02-22 03:15:00 | rand=65490

Auto-commit on 2025-02-22 14:54:54 | rand=61999

Auto-commit on 2025-02-22 15:07:00 | rand=85717

Auto-commit on 2025-02-22 15:19:05 | rand=93940

Auto-commit on 2025-02-22 15:31:11 | rand=17600

Auto-commit on 2025-02-22 15:43:11 | rand=1610

Auto-commit on 2025-02-22 15:55:17 | rand=28732

Auto-commit on 2025-02-22 16:07:22 | rand=28991

Auto-commit on 2025-02-22 16:19:21 | rand=77900

Auto-commit on 2025-02-22 16:31:22 | rand=90988

Auto-commit on 2025-02-22 16:43:23 | rand=58596

Auto-commit on 2025-02-22 16:55:27 | rand=60123

Auto-commit on 2025-02-22 17:07:26 | rand=22496

Auto-commit on 2025-02-22 17:19:37 | rand=45482

Auto-commit on 2025-02-22 17:31:37 | rand=98991

Auto-commit on 2025-02-22 17:43:43 | rand=34671

Auto-commit on 2025-02-24 13:58:31 | rand=26798

Auto-commit on 2025-02-24 14:10:32 | rand=92302

Auto-commit on 2025-02-24 14:22:32 | rand=91488

Auto-commit on 2025-02-24 14:34:39 | rand=73169

Auto-commit on 2025-02-24 14:46:47 | rand=72266

Auto-commit on 2025-02-24 14:58:47 | rand=19722

Auto-commit on 2025-02-24 15:10:54 | rand=42605

Auto-commit on 2025-02-24 15:22:56 | rand=45388

Auto-commit on 2025-02-24 15:35:06 | rand=37672

Auto-commit on 2025-02-24 15:47:16 | rand=83570

Auto-commit on 2025-02-24 15:59:25 | rand=39334

Auto-commit on 2025-02-24 16:11:26 | rand=50106

Auto-commit on 2025-02-24 16:23:22 | rand=14595

Auto-commit on 2025-02-24 16:35:29 | rand=93547

Auto-commit on 2025-02-24 16:47:33 | rand=5619

Auto-commit on 2025-02-24 17:59:47 | rand=36104

Auto-commit on 2025-02-24 18:11:47 | rand=14031

Auto-commit on 2025-02-24 18:23:53 | rand=51547

Auto-commit on 2025-02-24 18:35:58 | rand=21729

Auto-commit on 2025-02-24 18:48:05 | rand=77384

Auto-commit on 2025-02-24 19:00:08 | rand=29670

Auto-commit on 2025-02-24 19:12:20 | rand=29942

Auto-commit on 2025-02-24 19:24:24 | rand=98953

Auto-commit on 2025-02-24 19:36:23 | rand=21770

Auto-commit on 2025-02-24 19:48:24 | rand=32825

Auto-commit on 2025-02-24 20:00:28 | rand=14413

Auto-commit on 2025-02-24 20:12:34 | rand=88602

Auto-commit on 2025-02-24 20:24:38 | rand=50731

Auto-commit on 2025-02-24 20:36:42 | rand=95962

Auto-commit on 2025-02-24 20:48:41 | rand=51112

Auto-commit on 2025-02-25 12:22:25 | rand=74352

Auto-commit on 2025-02-25 12:34:24 | rand=78160

Auto-commit on 2025-02-25 12:46:33 | rand=58746

Auto-commit on 2025-02-25 12:58:33 | rand=1373

Auto-commit on 2025-02-25 13:10:36 | rand=49666

Auto-commit on 2025-02-25 13:22:43 | rand=91567

Auto-commit on 2025-02-25 13:34:51 | rand=93205

Auto-commit on 2025-02-25 13:46:49 | rand=42374

Auto-commit on 2025-02-25 13:58:53 | rand=21801

Auto-commit on 2025-02-25 14:10:54 | rand=63648

Auto-commit on 2025-02-25 14:23:00 | rand=77472

Auto-commit on 2025-02-25 14:35:03 | rand=58725

Auto-commit on 2025-02-25 14:47:11 | rand=69405

Auto-commit on 2025-02-25 14:59:14 | rand=82215

Auto-commit on 2025-02-25 15:11:22 | rand=24888

Auto-commit on 2025-03-06 14:52:22 | rand=37151

Auto-commit on 2025-03-06 15:03:45 | rand=45767

Auto-commit on 2025-03-06 15:15:03 | rand=43695

Auto-commit on 2025-03-06 15:51:27 | rand=53419

Auto-commit on 2025-03-06 16:02:42 | rand=473

Auto-commit on 2025-03-06 16:14:04 | rand=15681

Auto-commit on 2025-03-06 16:25:18 | rand=92919

Auto-commit on 2025-03-06 16:36:36 | rand=35104
