// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: 'REST Against Humanity',
    url: 'https://rest-against-humanity-celsiusnarhwal.vercel.app',
    baseUrl: '/',
    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',

    i18n: {
        defaultLocale: 'en',
        locales: ['en'],
    },

    presets: [
        [
            'classic',
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
                docs: {
                    sidebarPath: require.resolve('./sidebars.js'),
                },
                theme: {
                    customCss: require.resolve('./src/css/custom.css'),
                },
            }),
        ],
    ],

    themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
            navbar: {
                title: 'REST Against Humanity',
                items: [
                    {
                        href: 'https://github.com/celsiusnarhwal/rest-against-humanity',
                        label: 'GitHub',
                        position: 'right',
                    },
                ],
            },
            footer: {
                style: 'dark',
                copyright: `<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />The contents of this site are licensed under a <a rel="license" href="/docs/license">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
                            <br><br>
                            REST Against Humanity © ${new Date().getFullYear()} celsius narhwal. REST Against Humanity is not affiliated with or endorsed by Cards Against Humanity, LLC.`,
            },
            prism: {
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme,
                additionalLanguages: ['java', 'kotlin', 'swift', 'ruby'],
            },
        }),
};

module.exports = config;
