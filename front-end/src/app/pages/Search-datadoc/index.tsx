import React from "react";

import AppSearchAPIConnector from "@elastic/search-ui-app-search-connector";

import {
  ErrorBoundary,
  Facet,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  Sorting,
  WithSearch,
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";
import ClearFilter from './CustomFilter';
import { toAbsoluteUrl } from '../../../_metronic/helpers'
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
import {
  buildAutocompleteQueryConfig,
  buildFacetConfigFromConfig,
  buildSearchOptionsFromConfig,
  buildSortOptionsFromConfig,
  getConfig,
  getFacetFields
} from "./config-helper";
import { SearchDriverOptions, SearchResult } from "@elastic/search-ui";
import "./style.css";
const { hostIdentifier, searchKey, endpointBase, engineName } = getConfig();

const connector = new AppSearchAPIConnector({
  searchKey,
  engineName,
  hostIdentifier,
  endpointBase
});
const config: SearchDriverOptions = {
  searchQuery: {
    facets: buildFacetConfigFromConfig(),
    ...buildSearchOptionsFromConfig()
  },
  autocompleteQuery: buildAutocompleteQueryConfig(),
  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};
const imageOnErrorHandler = (
  event: React.SyntheticEvent<HTMLImageElement, Event>
) => {
  event.currentTarget.src = toAbsoluteUrl('/media/stock/600x400/img-26.jpg');
  event.currentTarget.className = "error";
};
export default function App() {
  const intl = useIntl()
  return (
    <>
    <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.SEARCHDATADOC' })}</PageTitle>
    
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox autocompleteSuggestions={true} />}
                  sideContent={
                    <div>
                      <ClearFilter />
                      <br />
                      {wasSearched && (
                        <Sorting
                          label={"Sort by"}
                          sortOptions={buildSortOptionsFromConfig()}
                        />
                      )}
                      {getFacetFields().map((field: any, index: number) => (
                        <Facet key={field} field={field} label={field} />
                      ))}
                    </div>
                  }
                  bodyContent={
                    <Results
                      resultView={CustomResultView}
                      titleField={getConfig().titleField}
                      urlField={getConfig().urlField}
                      thumbnailField={getConfig().thumbnailField}
                      shouldTrackClickThrough={true}
                    />
                  }
                  bodyHeader={
                    <React.Fragment>
                      {wasSearched && <PagingInfo />}
                      {wasSearched && <ResultsPerPage />}
                    </React.Fragment>
                  }
                  bodyFooter={<Paging />}
                />
              </ErrorBoundary>
            </div>
          );
        }}
      </WithSearch>
    </SearchProvider>
    </>
  );
}
const CustomResultView = ({
  result,
  onClickLink
}: {
  result: SearchResult;
  onClickLink: () => void;
}) => (
  <li className="sui-result">

    <div className="sui-result__header">
      <div className="sui-result__image">
        <img src={result.feature_image.raw} alt="" onError={imageOnErrorHandler} />
      </div>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <div className="sui-result__details">
          <h3>
            <a onClick={onClickLink} href={result.href.raw}>
              {result.topic.raw}
            </a>
          </h3>
        </div>

        <div className="sui-result__body" style={{ display: 'flex', flexDirection: 'column' }}>
          <span
            className="sui-result__details"
            dangerouslySetInnerHTML={{ __html: result.sapo.raw }}
          >
          </span>
          <div
            className="sui-result__details"
            dangerouslySetInnerHTML={{ __html: result.publish_date.raw }}
          >
          </div>
        </div>
      </div>
    </div>


  </li>
);

