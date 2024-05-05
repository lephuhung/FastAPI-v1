import { withSearch } from "@elastic/react-search-ui";
type Search={
    filters:string,
    clearFilters: ()=>void
}
function ClearFilters({ filters, clearFilters }:Search)  {
  return (
    <div>
      <button className="btn btn-primary" onClick={() => clearFilters()}>
        Clear {filters.length} Filters
      </button>
    </div>
  );
}

export default withSearch(({ filters, clearFilters }) => ({
  filters,
  clearFilters
}))(ClearFilters);
