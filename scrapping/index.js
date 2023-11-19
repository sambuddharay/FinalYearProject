const fs = require("fs");
const puppeteer = require("puppeteer");
const {
  URLSTAT_LIST,
  URLSTAT_TO_TABLEID_MAP,
  LEAGUE_LIST,
  SEASON_LIST,
  LEAGUE_TO_ID,
} = require("./constants");

let browser;

(async () => {
  // Launch the browser and open a new blank page
  try {
    browser = await puppeteer.launch({
      headless: "new",
      defaultViewport: false,
      userDataDir: "./tmp ",
    });

    for (let i = 0; i < LEAGUE_LIST.length; i++) {
      const league = LEAGUE_LIST[i];
      for (let j = 0; j < SEASON_LIST.length; j++) {
        const season = SEASON_LIST[j];
        for (let k = 0; k < URLSTAT_LIST.length; k++) {
          const statType = URLSTAT_LIST[k];
          const page = await browser.newPage();
          await scrapData(
            LEAGUE_TO_ID[league],
            season,
            statType,
            league,
            URLSTAT_TO_TABLEID_MAP[statType],
            page
          );
          page.close();
        }
      }
    }
  } catch (err) {
    console.log(err);
  } finally {
    browser?.close();
  }
})();

const scrapData = async (leagueId, season, statType, league, tableId, page) => {
  // Navigate the page to a URL
  await page.goto(
    `https://fbref.com/en/comps/${leagueId}/${season}/${statType}/${season}-${league}`,
    { timeout: 0 }
  );

  // TABLE HEADER
  const tableTopHeader = await page.$eval(
    `#${tableId} > thead > tr:nth-child(1)`,
    (el) => {
      const tableTopHeader = [];
      Array.from(el.children).forEach((element) => {
        for (let i = 0; i < element.colSpan; i++) {
          tableTopHeader.push(element.innerText.replace(/,/g, "").trim());
        }
      });
      return tableTopHeader;
    }
  );
  const tableHeader = await page.$eval(
    `#${tableId} > thead > tr:nth-child(2)`,
    (el) =>
      Array.from(el.children)
        .slice(0, -1)
        .map((element) => element.innerText.replace(/,/g, "").trim())
  );
  const tableFinalHeader = tableHeader.map((val, index) =>
    (tableTopHeader[index] + " " + val).trim()
  );

  //TABLE CONTENT
  const tableData = await page.$eval(
    `#${tableId} > tbody`,
    (el, tableHeader) => {
      const tableData = [];
      Array.from(el.children).forEach((row) => {
        const col = Array.from(row.children);
        const rowData = [];
        col.slice(0, -1).forEach((elem, index) => {
          let content;
          if (index === 3) {
            //for positions played "," is replaced with "|"
            content = elem.innerText.replace(/,/g, "|").trim();
          } else {
            content = elem.innerText.replace(/,/g, "").trim();
          }
          rowData.push(content);
        });
        if (JSON.stringify(rowData) === JSON.stringify(tableHeader)) return;
        //Replace the nation data item to nation code only
        const NATION = rowData[2].split(" ")[1];
        rowData[2] = NATION;
        tableData.push(rowData);
      });
      return tableData;
    },
    tableHeader
  );

  //WRITING CONTENT TO FILE
  const dir = `./data/${league}/${season}/`;
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const FILENAME = `./data/${league}/${season}/${league}-${season}-${statType}.csv`;
  console.log(`created file: ${FILENAME}`);
  fs.writeFileSync(FILENAME, tableFinalHeader.join(",") + "\n");
  console.log(`created header: ${tableFinalHeader.join(",")}`);
  tableData.forEach((row) => {
    fs.appendFileSync(FILENAME, row.join(",") + "\n");
    console.log(`inserted: ${row.join(",")}`);
  });
  console.log(`inserted ${tableData.length} rows`);
};
