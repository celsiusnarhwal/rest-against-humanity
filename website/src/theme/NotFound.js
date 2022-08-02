import React from 'react';
import {translate} from '@docusaurus/Translate';
import {PageMetadata} from '@docusaurus/theme-common';
import Layout from '@theme/Layout';

export default function NotFound() {
    return (
        <>
            <PageMetadata
                title={translate({
                    id: 'theme.NotFound.title',
                    message: 'Page Not Found',
                })}
            />
            <Layout>
                <main className="container margin-vert--xl">
                    <div className="row">
                        <div className="col col--6 col--offset-3">
                            <h1 className="hero__title">
                                Wrong turn.
                            </h1>
                            <p>
                                That page doesn't exist.
                            </p>
                            <p>
                                If you were linked here by someone from outside of this site, tell them their link
                                is broken. If you typed in the URL yourself, check your spelling. If you were linked
                                here from elsewhere on this site, or are otherwise confident that a page should
                                definitely exist here, please <a
                                href="https://github.com/celsiusnarhwal/rest-against-humanity/issues">open an issue on
                                GitHub</a>.
                            </p>
                        </div>
                    </div>
                </main>
            </Layout>
        </>
    );
}
