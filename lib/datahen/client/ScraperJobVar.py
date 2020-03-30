from lib.datahen.client.Base import Base
import  json

class ScraperJobVar(Base):
    def find(self, scraper_name, var_name):
        return self.get(
            "/scrapers/{}/current_job/vars/{}".format(scraper_name, var_name),
            self._options)

    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get(
            "/scrapers/{}/current_job/output/collections/{}/records".format(scraper_name), opts)

    def set(self,scraper_name, var_name, value, opts={}):
        body = {}
        body['value'] = value
        if 'secret' in opts and opts['secret']: body['secret'] = opts['secret']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.put("/scrapers/{}/current_job/vars/{}".format(scraper_name, var_name), opts)


    def unset(self, scraper_name, var_name, opts={}):
        opts.update(self._options)
        return self.delete(
            "/scrapers/{}/current_job/vars/{}".format(scraper_name, var_name), opts)