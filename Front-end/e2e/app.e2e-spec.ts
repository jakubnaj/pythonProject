import { AdviseMePage } from './app.po';

describe('advise-me App', () => {
  let page: AdviseMePage;

  beforeEach(() => {
    page = new AdviseMePage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
