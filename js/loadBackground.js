/**
 * @author
 * ISAB Dev Team
 * @description
 * Awesome background images for ISAB pages.
 * The latest version can always be found here:
 * https://github.com/urlib/static.isab.top/blob/master/js/loadBackground.js
 * You can Load this file from jsDelivr:
 * https://cdn.jsdelivr.net/gh/urlib/static.isab.top@latest/js/loadBackground.js
 * There is also a minified version (thanks to jsDelivr):
 * https://cdn.jsdelivr.net/gh/urlib/static.isab.top@latest/js/loadBackground.min.js
 */

(() => {
    const rootUrl = 'https://cdn.jsdelivr.net/';
    const backgroundImageList = [
        {
            name: 'Galaxy',
            origin: 'gh/urlib/bin_0@f5a296f9/fe/94/83/5f/fe94835f3f8985e5965b9fe974d1917858affba03182c2aef5071ffbfcaee61c.png',
            webp: 'gh/urlib/bin_0@f5a296f9/95/11/c2/d9/9511c2d95bdce8999a519c9f7c1910b316c4c6728bf6b7ef7ee9cdfd1a0faeb1.webp'
        },
        {
            name: 'Purple Galaxy',
            origin: 'gh/urlib/bin_0@f5a296f9/db/2e/1e/54/db2e1e54c1152b4dfef159d9668427876d7f5cd0a1a8e8caa83afa83cb4914de.png',
            webp: 'gh/urlib/bin_0@f5a296f9/fa/8b/c2/54/fa8bc254ad36808b3bf8d110e11678acb4206c07f12f95ff5d23d8920268259d.webp'
        }
    ];

    const completeUrl = (partialUrl) => {
        return `${rootUrl}${partialUrl}`;
    };
    const checkWebpSupport = () => {
        return document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp') == 0;
    };
    const isWebpSupported = checkWebpSupport();
    const randomChoice = (list) => {
        list.push(list.shift());
        return list[Math.floor(Math.random() * list.length)];
    };
    const imageChoice = (isWebpSupported) => {
        const image = randomChoice(backgroundImageList);
        return completeUrl(isWebpSupported ? image.webp : image.origin);
    };
    const imageUrl = imageChoice(isWebpSupported);

    window.addEventListener('load', () => {
        document.body.style.backgroundImage = `url(${imageUrl})`;
    });
})();
